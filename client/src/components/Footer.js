import React from 'react';

const Footer = () => (
  <footer className="cookie-bar">
    <p>
      By using this website, you agree to our use of cookies.{' '}
      <a href="/privacy">Privacy Policy</a>
    </p>
    <div className="buttons">
      <button>REFUSE</button>
      <button>ACCEPT</button>
    </div>
  </footer>
);

export default Footer;
