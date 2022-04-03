import React from "react";
import {Link} from "react-router-dom";


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`/user/${user.id}`}>{user.username}</Link>
            </td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.birthday}</td>
            <td>{user.email}</td>
            <td>{user.is_superuser.toString()}</td>
            <td>{user.is_staff.toString()}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>Username</th>
            <th>First name</th>
            <th>Last name</th>
            <th>Birthday</th>
            <th>Email</th>
            <th>ISsuperuser</th>
            <th>ISstaff</th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}

export default UserList
