import React from 'react';

function Signin() {
  return (
    <>
      <div className="signin-div">
        <div className="signin-username-div">
          <label htmlFor="signin-username">Username</label>
          <input type="text" name="username" id="signin-username" />
        </div>
        <div className="signin-password-div">
          <label htmlFor="signin-password">Password</label>
          <input type="password" name="password" id="singin-password" />
        </div>
        <div className="signin-button-div">
          <button type="submit">Login</button>
        </div>
      </div>
    </>
  )
}

export default Signin