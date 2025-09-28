import {useEffect, useState} from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './features/auth/login'
import Dashboard from './features/dashboard/Dashboard'
import Register from './features/auth/register'
import './App.css';
import React from "react";

function App() {
const [user,setUser] = useState(null);

useEffect(()=>{
  const savedUser = localStorage.getItem('user');
  if(savedUser)setUser(JSON.parse(savedUser));
},[])

const handleLogin = (userObjct: any) =>{
    console.log("called login")

localStorage.setItem('user',JSON.stringify(userObjct));
setUser(userObjct)
}

const handleLogout = ()=>{
  console.log("called logout")
  localStorage.removeItem('user');
  setUser(null);
}

  return (
   <Router>
    <Routes>
      <Route path="/" element={<Login onLogin={handleLogin}/>}></Route>
      <Route path = "/register" element = {<Register/>}/>
      <Route path ="/dashboard" element = {user? <Dashboard user={user} onLogout ={handleLogout}/> : <Navigate to="/"/>}/>

    </Routes>
   </Router>
  );
}

export default App;
