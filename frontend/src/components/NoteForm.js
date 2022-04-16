import React from 'react'

class NoteForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'project': 0,
            'text': ''
        }
    }

    handleSubmit(event) {
        this.props.newNote(this.state.project, this.state.text)
        event.preventDefault()
    }

    handleProjectChange(event) {
        if (!event.target.selectedOptions) {
            return
        }

        let project = []
        for (let i=0; i < event.target.selectedOptions.length; i++) {
            project.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'project': project[0]
        })
    }

    handleTextChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)} >
                <input
                    type="text"
                    name="text"
                    placeholder="text"
                    onChange={(event) => this.handleTextChange(event)}
                    value={this.state.text}
                />
                <select onChange={(event) => this.handleProjectChange(event)}>
                    {this.props.project.map((project) => <option value={project.id}>{project.project_name}</option>)}
                </select>

                <input type="submit" value="Create" />
            </form>
        )
    }
}

export default NoteForm