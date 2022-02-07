import './App.css';
import {Component} from "react";

class App extends Component{
    constructor(props) {
        super(props);
        this.state={
                username:'',
                password:'',
                status:false,
            }
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
    this.setState({[event.target.name]:event.target.value});
  }

    handleSubmit(event) {
    console.log('Сочинение отправлено:');
    console.log(this.state)
          fetch('http://127.0.0.1:8000/api/token/',{
        method: "POST", // POST, PUT, DELETE, etc.
        headers: {
            "Content-Type": "application/json"},
            body:JSON.stringify({"username":this.state.username, "password":this.state.password})
                 })
        .then(response=>{
            if(response.status!==200){
                 console.log(response.status)
            }else {
                this.setState({status:true})
                return response.json()}})
        .then(tokens=>{
            console.log(tokens)})}
    render() {
        if(this.state.status){
            return (
                <div>
                    <h1>Ты залогинился</h1>
                </div>
            )
        }else{
     return(
            <form action="" name={'first'}>
                <label htmlFor="">
                    Username
                </label>
                <input type="text" name={'username'} onChange={this.handleChange}/><br/>
                <label htmlFor=""> Password</label>
                <input type="text" name={'password'} onChange={this.handleChange}/><br/>
                <input type="button" onClick={this.handleSubmit} value={'ok'}/>
            </form>
            )        }

    }
}

export default App;