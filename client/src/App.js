import './App.css';
import Header from './components/Header';
import Hero from './components/Hero';
import Content from './components/Content';
import ThankYou from './components/ThankYou';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header />
      <Hero />
      <Content />
      <ThankYou />
      <Footer />
    </div>
  );
}

export default App;
