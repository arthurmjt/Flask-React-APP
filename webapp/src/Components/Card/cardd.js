import React from 'react';

export const Card = ({ listOfTodos})=> {
    return(
        <>
            <p>TOP related institutions for an input institution:</p>
            {listOfTodos.map(todo => {
                return(
                    <ul key={todo.id}>
                        <li>
                            Affiliation's ID: {todo.affiliation_id}&nbsp;
                            Amount: {todo.affiliation_amount}
                        </li>
                    </ul>
                )
            })

            }
        </>
        )





}