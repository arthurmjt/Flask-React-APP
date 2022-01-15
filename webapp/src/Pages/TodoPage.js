import React, {useState, useEffect} from 'react';
import {Card} from '../Components/Card/card';
import {Form} from '../Components/Form/form';

export const TodoPage = ()=> {

    const [todo, setTodo] = useState([])
    const [addTodo, setAddTodo] = useState('')

    useEffect(()=> {
            fetch('/paper').then(response => {
                if(response.ok){
                    return response.json()
                }
            }).then(data => setTodo(data))
        },[])

    const handleFormChange = (inputValue) => {
        setAddTodo(inputValue)
        console.log(addTodo)
    }

    const handleFormSubmit = () => {
        fetch('/paper/submit', {
            method: 'POST',
            body: JSON.stringify({
                content:addTodo
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }).then(response => response.json())
            .then(message => {
                console.log(message)
                setAddTodo('')})
    }

    const getLatestTodos = () => {
        fetch('/paper').then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => setTodo(data))
    }



    return(
        <>
            <Form userInput={addTodo} onFormChange={handleFormChange} onFormSubmit={handleFormSubmit}/>
            <Card listOfTodos={todo} onCardChange={getLatestTodos}/>
        </>
    )
}
