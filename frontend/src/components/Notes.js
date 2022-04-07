import React from "react";


const NoteItem = ({note}) => {
    return (
        <tr>
            <td>{note.id}</td>
            <td>{note.project}</td>
            <td>{note.text}</td>
        </tr>
    )
}

const NotesList = ({notes}) => {
    return (
        <table>
            <th>запись №</th>
            <th>к проекту №</th>
            <th>содержание</th>
            {notes.map((note) => <NoteItem note={note}/>)}
        </table>
    )
}

export default NotesList
