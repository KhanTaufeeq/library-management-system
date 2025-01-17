import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Signup() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [userName, setUserName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [contact, setContact] = useState('');
  // const [csrfToken, setCsrfToken] = useState('')

  const navigate = useNavigate();

  // const getCSRFToken = () => {
  //   axios.get('http://127.0.0.1:8000/user/csrf/', {
  //     withCredentials: true,
  //   })
  //   .then((response) => {
  //     console.log(response.data.csrfToken);
  //     setCsrfToken(response.data.csrfToken);
  //   })
  //   .catch((error) => {
  //     console.log(error)
  //   })
  // }

  // const getCSRFToken = () => {
  //   const csrfToken = document.cookie
  // .split('; ')
  // .find(row => row.startsWith('csrftoken='))
  // ?.split('=')[1];
  // }

  useEffect(() => {
    getCSRFToken();
  }, [])

  const doSignUp = () => {
    axios.post('http://127.0.0.1:8000/user/signup/', {
      'first_name': firstName,
      'last_name' : lastName,
      'username' : userName,
      'email' : email,
      'password' : password,
      'contact' : contact,
    },
    {
      headers : {
        'Content-Type': 'application/json',
        'X-CSRFToken' : csrfToken,
      },
      withCredentials: true,
    }
  )
    .then((response) => {
      console.log('Signup Successfull: ', response.data);
      navigate('/signin');
    })
    .catch((error) => {
      console.log('Error during Signup: ',error)
    })
  }


  return (
    <>
      <div className="signup-div">
        <div className="first-name">
          <label htmlFor="first-name">First Name</label>
          <input type="text" name="first-name" id="first-name" onChange={(event) => setFirstName(event.target.value)}/>
        </div>
        <div className="last-name">
          <label htmlFor="last-name">Last Name</label>
          <input type="text" name="last-name" id="last-name" onChange={(event) => setLastName(event.target.value)}/>
        </div>
        <div className="username">
          <label htmlFor="username">Username</label>
          <input type="text" name="username" id="username" onChange={(event) => setUserName(event.target.value)}/>
        </div>
        <div className="email">
          <label htmlFor="email">Email</label>
          <input type="email" name="email" id="email" onChange={(event) => setEmail(event.target.value)}/>
        </div>
        <div className="password">
          <label htmlFor="password">Password</label>
          <input type="password" name="password" id="password" onChange={(event) => setPassword(event.target.value)}/>
        </div>
        <div className="contact">
          <label htmlFor="contact">Contact Number</label>
          <input type="text" name="contact" id="contact" onChange={(event) => setContact(event.target.value)}/>
        </div>
        <div className="submit-div">
          <button type="submit" onClick={doSignUp}>
            Register
          </button>
        </div>
      </div>
    </>
  )
}

export default Signup;