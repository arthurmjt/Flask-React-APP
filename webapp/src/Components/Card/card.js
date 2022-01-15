import React from 'react';

export const Card = ({ listOfTodos, onCardChange})=> {
    return(
        <>
            <p>TOP papers that an author most often cites in their own papers:</p>
            {listOfTodos.map(todo => {
                return(
                    <ul key={todo.id}>
                        <li onChange={onCardChange}>
                            Paper's ID: {todo.paper_id}&nbsp;
                            Paper's citations: {todo.paper_num}
                        </li>
                    </ul>
                )
            })

            }
        </>
        )





}