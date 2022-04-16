import React from 'react'

class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'project_name': '',
            'users': ''
        }
    }

    handleSubmit(event) {
        this.props.newProject(this.state.project_name, this.state.users)
        event.preventDefault()
    }

    handleUserChange(event) {
        if (!event.target.selectedOptions) {
            return
        }

        let users = []
        for (let i=0; i < event.target.selectedOptions.length; i++) {
            users.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'users': users
        })
    }

    handleProjectNameChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)} >
                <input
                    type="text"
                    name="project_name"
                    placeholder="project_name"
                    onChange={(event) => this.handleProjectNameChange(event)}
                    value={this.state.project_name}
                />
                <select multiple onChange={(event) => this.handleUserChange(event)}>
                    {this.props.users.map((user) => <option value={user.id}>{user.first_name} {user.last_name}</option>)}
                </select>
                <input type="submit" value="Create" />
            </form>
        )
    }
}

export default ProjectForm