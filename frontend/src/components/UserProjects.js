import React from "react";
import {useParams} from "react-router-dom";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.project_name}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const UserProjects = ({projects}) => {
    let {id} = useParams()
    let filteredProjects = projects.filter((project) => project.users.includes(parseInt(id)))

    return (
        <table>
            <th>№ проекта</th>
            <th>название проекта</th>
            <th>в проекте участвуют</th>
            {filteredProjects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default UserProjects
