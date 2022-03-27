import React from 'react';
// import logo from './logo.svg';
import './App.css';
import UserList from './components/Users';
import ProjectsList from "./components/Projects";
import NotesList from "./components/Notes";
import UserProjects from "./components/UserProjects";
import ProjectsNotes from "./components/ProjectsNotes";
import LoginForm from "./components/LoginForm";
import axios from "axios";
import {HashRouter, BrowserRouter, Route, Routes, Link, useLocation, Navigate} from 'react-router-dom'

const NotFound = () => {
    let location = useLocation()
    return (
        <div>
            <hr/>
            Page {location.pathname} not found
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [
                // {
                //     "username": "taran",
                //     "first_name": "Квентин",
                //     "last_name": "Тарантино",
                //     "birthday": "1963-03-27",
                //     "email": "quen-taran@mail.ru"
                // },
                // {
                //     "username": "Stan",
                //     "first_name": "Стэнли",
                //     "last_name": "Кубрик",
                //     "birthday": "1928-06-26",
                //     "email": "stan-kubrick@mail.ru"
                // },
                // {
                //     "username": "Bob",
                //     "first_name": "Роберт",
                //     "last_name": "Земекис",
                //     "birthday": "1951-05-14",
                //     "email": "zem-rob@mail.ru"
                // }, {
                //     "username": "Стив",
                //     "first_name": "Стивен",
                //     "last_name": "Спилберг",
                //     "birthday": "1946-12-18",
                //     "email": "ono-it@mail.ru"
                // }, {
                //     "username": "Пит",
                //     "first_name": "Питер",
                //     "last_name": "Джексон",
                //     "birthday": "1961-10-31",
                //     "email": "pit-jec@mail.ru"
                // }, {
                //     "username": "Клинт",
                //     "first_name": "Клинт",
                //     "last_name": "Иствуд",
                //     "birthday": "1930-05-31",
                //     "email": "good-bad-ugly@mail.ru"
                // }
                //
            ],
            'projects': [],
            'notes': [],
            'token': ''
        }
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'users': []
                })
            })
        axios
            .get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState(
                    {
                        'projects': []
                    }
                )
            })
        axios
            .get('http://127.0.0.1:8000/api/notes/', {headers})
            .then(response => {
                const notes = response.data
                this.setState(
                    {
                        'notes': notes
                    }
                )
            })
            .catch(error => {
                    console.log(error)
                    this.setState(
                        {
                            'notes': []
                        })
                }
            )

    }


    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {'username': login, 'password': password})
            .then(response => {
                const token = response.data.token
                // console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token,
                }, this.getData)
            })
            .catch(error => console.log(error))

        // console.log(login, password)
    }


    logout() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    render() {
        return (
            <div>
                <>Menu</>
                <hr/>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Users</Link></li>
                        <li><Link to='/projects'>Projects</Link></li>
                        <li><Link to='/notes'>Notes</Link></li>
                        <li>
                            {this.isAuth() ? <button onClick={() => this.logout()}>Logout</button> :
                                <Link to='/login'>Login</Link>}
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<UserList users={this.state.users}/>}/>
                        <Route exact path='/login'
                               element={<LoginForm getToken={(login, password) => this.getToken(login, password)}/>}/>
                        <Route exact path='/users' element={<Navigate to='/'/>}/>
                        <Route exact path='/projects' element={<ProjectsList projects={this.state.projects}/>}/>
                        <Route exact path='/notes' element={<NotesList notes={this.state.notes}/>}/>
                        <Route exact path='/user/:id' element={<UserProjects projects={this.state.projects}/>}/>
                        <Route exact path='/project/:id' element={<ProjectsNotes notes={this.state.notes}/>}/>
                        <Route exact path='*' element={<NotFound/>}/>
                    </Routes>
                </BrowserRouter>
                <hr/>
                <>footer</>
            </div>
        )
    }
}


// import logo from './logo.svg';
// import './App.css';
//
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
//


export default App;
