import React from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>
                <Link to={`/project/${project.id}`}>{project.project_name}</Link>
            </td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectsList = ({projects}) => {
    return (
        <table>
            <th>№ проекта</th>
            <th>название проекта</th>
            <th>в проекте участвуют</th>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default ProjectsList
