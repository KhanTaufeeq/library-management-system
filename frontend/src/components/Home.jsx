import React from 'react';
import {Link} from 'react-router-dom';

function Home() {
  return (
    <>
      <h1>Find your favorite books here...</h1>
      <p>just once click <Link to='/signup'>register</Link> away</p>
    </>
  )
}

export default Home