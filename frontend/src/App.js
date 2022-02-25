import React from 'react';
// import logo from './logo.svg';
import './App.css';
import UserList from './components/Users';
import axios from "axios";


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
            ]
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1.8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <UserList users={this.state.users}/>
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
