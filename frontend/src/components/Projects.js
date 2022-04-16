import React from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>
                <Link to={`/project/${project.id}`}>{project.project_name}</Link>
            </td>
            <td>{project.users}</td>
            <td>
                <button onClick={()=>deleteProject(project.id)}>Delete</button>
            </td>
        </tr>
    )
}

const ProjectsList = ({projects, deleteProject}) => {
    return (
        <table>
            <th>№ проекта</th>
            <th>название проекта</th>
            <th>в проекте участвуют</th>
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
        </table>
    )
}

export default ProjectsList
