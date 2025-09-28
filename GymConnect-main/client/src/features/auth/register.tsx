import React from "react";
import { useNavigate } from "react-router-dom";
import './styles/register.css'

export default function Register(){
const [username, setUsername]= React.useState('');
const [firstname, setFirstname]= React.useState('');
const [lastname, setLastname]= React.useState('');
const navigate = useNavigate();


const handleRegistration = ()=>{
 // You could add form validations
    alert('User registered (not actually saved in this demo)');
    navigate('/');
}

return (
    <div className="register-page">
        <h3>New user Registration</h3>
        <input placeholder="User name" onChange={(e)=>setUsername(e.target.value)}/>
        <input placeholder="First name" onChange={(e)=>setFirstname(e.target.value)}/>
        <input placeholder="Last name" onChange={(e)=>setLastname(e.target.value)}/>
        <button className="btn btn-primary" onClick={handleRegistration}>Register</button>
    </div>
);


}