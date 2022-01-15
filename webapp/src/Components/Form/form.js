import React from 'react';

export const Form = ({ userInput, onFormChange, onFormSubmit })=> {

    const handleChange = (event) => {
        onFormChange(event.target.value)
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        onFormSubmit()
    }
    return(
        <>
            <form onSubmit={handleSubmit}>
                <label>Input An Author's ID: </label>
                <input type='text' required value={userInput} onChange={handleChange} />
                <input type='submit' value={"Submit"}/>
            </form>
        </>
    )
}