import React from "react";
import {useParams} from "react-router-dom";


const NoteItem = ({note}) => {
    return (
        <tr>
            <td>{note.id}</td>
            <td>{note.project}</td>
            <td>{note.text}</td>
        </tr>
    )
}

const ProjectsNotes = ({notes}) => {
    let {id} = useParams()
    let filteredNotes = notes.filter((note) => note.project == id)

    return (
        <table>
            <th>запись_№</th>
            <th>к проекту №</th>
            <th>содержание</th>
            {filteredNotes.map((note) => <NoteItem note={note}/>)}
        </table>
    )
}

export default ProjectsNotes
