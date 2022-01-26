import './App.css';
import {Component} from "react";

class App extends Component{
    constructor(props) {
        super(props);
        this.state={
        all_car:[],
        }
    }
    componentDidMount() {
    fetch('http://127.0.0.1:8000/car/')
    .then(response=>response.json())
    .then(cars=>{
    for (let i of cars){
    console.log(i.brand, i.model)}
    this.setState({all_car:cars})
    })
    }
    render() {
    onsole.log(this.state)
    return(
    <div>
    <p1> {this.state.all_car} </p1>
    </div>
     )

    }
}

export default App;
