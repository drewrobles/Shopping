import { useEffect, useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import styles from './index.module.css'

import quizQuestionData from '../quizQuestionData'
import Navbar from '../components/Navbar/Navbar'
import Header from '../components/Header/Header'
import Content from '../components/Content/Content'
import Control from '../components/Control/Control'
import Results from '../components/Modal/Modal'
import Button from '../components/Button/Button'

const quizTitle='Weird Text Format Encoder'
const quizDescription='Your shopping list is empty :('
const estimatedTime='30 minutes'
const difficultyLevel='6'
const answerKey=['a1', 'b2', 'c3', 'd4', 'e4']

export default function Home() {
  const [state, setState] = useState({
    'input': '',
    'decodeInput': ''
  })

  
  
  const handleEncode = (e, state) => {
    e.preventDefault()
    const baseUrl = 'http://localhost:8000'
    fetch(baseUrl + '/encoder/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Origin': 'http://localhost:3000',
      },
      body: JSON.stringify({'text': state.input})
    }).then(res => res.json()).then(json => alert('Encoded value is: ' + json.encoded))
  }

  const handleDecode = (e, state) => {
    e.preventDefault()
    const baseUrl = 'http://localhost:8000'
    fetch(baseUrl + '/decoder/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Origin': 'http://localhost:3000',
      },
      body: JSON.stringify({'values': validateNumbersAndNotify(state.decodeInput) ? state.decodeInput.split(",").map(Number) : ''})
    }).then(res => res.json()).then(json => validateNumbers(state.decodeInput) ? alert('Decoded value is: ' + json.decoded) : {})
  }

  const handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };

  function getRequest(props) {
    alert('Input state is: ' + state.decodeInput)
  }

  
  return (
    <div className={`${styles.index}`}>
        <Navbar/>
      <form onSubmit={e => handleDecode(e, state)} className={`container`}>
          <div className={`mt-5`}>
            <Header 
              quizDescription={quizDescription}
              questionIndex={state.questionIndex}
            />
          </div>
          <Status
              questionIndex={state.questionIndex}
              quizLength={quizQuestionData.length}
          />

          
          <div>
            <Button buttonText={'Add your first item'}/>
          </div>
      </form>
    </div>
  )
}

const validateNumbers = (myString) => {
  let regex = /[0-9]+(,[0-9]+)*/g
  if (regex.test(myString)) {
    return true
  } else {
    return false
  }
}

const validateNumbersAndNotify = (myString) => {
  if (validateNumbers(myString)) {
    return true
  } else {
    alert('List of numbers to decode was invalidly formatted. Please try again.')
    return false
  }
}


function Status(props) {
  const keys = [...Array(props.quizLength).keys()]
  if (props.questionIndex >=0 ) {
    // Add one to zero indexed question number
    return <div>
      <div class="d-flex flex-row-reverse">
        <div class="p-2"><nav aria-label="Page navigation example">
            <ul class="pagination">
              {
                keys.map(currKey => currKey == props.questionIndex ? 
                <li class="page-item active"><a class="page-link" href="#">{currKey + 1}</a></li>:
                <li class="page-item"><a class="page-link" href="#">{currKey + 1}</a></li>)
              }
            </ul>
          </nav>
        </div>
      </div>
    </div>
  } else return <></>
}