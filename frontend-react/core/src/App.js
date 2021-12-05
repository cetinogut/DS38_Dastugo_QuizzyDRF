import React from 'react'
//import Header from './components/framework/Header'
import {Route, Routes} from 'react-router-dom'
import { BrowserRouter as Router } from 'react-router-dom';
import QuizSelect from './components/QuizSelect'
import RandomQuiz from './components/RandomQuiz'


function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" component={QuizSelect} exact />
          <Route path="/r/:topic" component={RandomQuiz} exact />
        </Routes>
    </Router>
  );
}

export default App;
