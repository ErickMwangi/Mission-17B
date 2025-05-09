// Hero.js
import React from 'react';
import glassmorphism from '/home/maverick/Development/Projects/Mission-17B/client/src/images/coming soon.jpeg'; 

const Hero = () => (
  <section className="hero">
    <img src={glassmorphism} alt="Just Cause Y'all Waited" />
    <div className="content">
      <h1>Welcome to Mission 17B</h1>
      <p>Stay tuned for something amazing!</p>
    </div>
  </section>
);

export default Hero;
