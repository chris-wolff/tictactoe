import React from 'react';
import { BASE_URL } from './requests';

/*Child component of GameModeMenu*/
class CreateGame extends React.Component{

    // Props should be a gameMode, and a function pointer for a 
    // callback function which gets passed a JSON representation of 
    // the current game. 
    constructor(props){
        super();
        this.requestNewGameFromTTTServer = this.requestNewGameFromTTTServer.bind(this);

        this.state = {
            gameMode: "localGame"
        }
    }

    // Get the new props (game mode from Game Menu parent) and store it in state.
    UNSAFE_componentWillReceiveProps(newProps) {
        this.setState({gameMode: newProps.gameMode})
    }

    // Requests a new game to be started on the TicTacToe Python back-end. 
    // The new game has to be created with a GameMode
    // from the GameMode menu component.
    requestNewGameFromTTTServer(event){

        if (typeof this.state.gameMode !== "undefined"){
            let joined = BASE_URL +  '/games/?gameMode=' + this.state.gameMode;
            
            //fetch requests wraps everything in a promise
            fetch(joined, {method: 'POST'})
            .then(response => response.json())
            .then(json => this.props.callback(json))
            .catch(error => console.error(error)); 
        }
            
    }

    render(){
        return(<button type="button" className="btn btn-success" onClick = {this.requestNewGameFromTTTServer}>
                Create Game
            </button>);
    }
}

export default CreateGame;