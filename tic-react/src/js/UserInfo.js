import React, { Component } from 'react'; 
import {BASE_URL} from './requests'

class UserInfo extends Component{

    constructor(props){
        super()
        this.fetchUser = this.fetchUser.bind(this)
    }

    /**
     * Fetch the current authenticated user from the back-end.
     */
    fetchUser(){
        let joined = BASE_URL +  '/user'
            
        // Fetch requests wraps everything in a promise
        fetch(joined, {method: 'GET'})
        .then(response => response.text())
        .then(user => {console.log(user); return user})
        .catch(error => console.error(error)); 
    }

    render(){
        return(
            <div>You are currently logged in as: {this.fetchUser()}</div>
        )
    }
}


export default UserInfo;