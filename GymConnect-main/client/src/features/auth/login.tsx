import { useNavigate } from "react-router-dom";
import './styles/login.css'
import React from "react";

export default function LoginPage ( {onLogin}: {onLogin: (userObjct: any)=> void}){
const [username, setUsername]= React.useState('');
const navigate = useNavigate();

const handleLogin = () =>{
    if(username.trim()){
        const dummyUser = {
            username,
            role: username ==='admin'? 'admin' : 'user'
        };
        onLogin(dummyUser)
        navigate('/dashboard')
    }

}

return(
    <div className="login-page">
        <h2>Login</h2>
        <input placeholder="user name"   value={username}   onChange={(e)=>setUsername(e.target.value)}/>
        <button className="btn btn-primary" onClick={handleLogin}>Login</button>
         <p>
        Don't have an account? <a href="/register">Register</a>
      </p>
    </div>
);

}