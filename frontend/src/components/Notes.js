import React from "react";


const NoteItem = ({note, deleteNote}) => {
    return (
        <tr>
            <td>{note.id}</td>
            <td>{note.project}</td>
            <td>{note.text}</td>
            <td>
                <button onClick={()=>deleteNote(note.id)}>Delete</button>
            </td>
        </tr>
    )
}

const NotesList = ({notes, deleteNote}) => {
    return (
        <table>
            <th>запись №</th>
            <th>к проекту №</th>
            <th>содержание</th>
            {notes.map((note) => <NoteItem note={note} deleteNote={deleteNote}/>)}
        </table>
    )
}

export default NotesList
