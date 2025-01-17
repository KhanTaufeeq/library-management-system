import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Signin from "./components/Signin";
import Signup from "./components/Signup";

function Router() {
  return(
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element = {<Home/>} />
          <Route path='/signup' element = {<Signup/>} />
          <Route path='/signin' element={<Signin/>} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default Router;