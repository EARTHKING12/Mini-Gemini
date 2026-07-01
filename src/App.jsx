// import React, { useState } from 'react';
// function App() {
//   const [prompt, setPrompt] = useState('');
//   const[output, setOutput] = useState('');

// function handleChange(event) {
//     setPrompt(event.target.value);
//   }

// // console.log(prompt);
// async function generateResponse() {
//     const res = await axios.post("http://127.0.0.1:8000/generate", { prompt: prompt })
//       console.log(res.data.response);
//   }

//   return (
//     <div className="App">
//       <h1>Mini Gemini Project</h1>
//       <textarea
//         onChange={handleChange} placeholder="Enter your text here..."
//         rows={10}
//         cols={50}
//       ></textarea>
//       <br />
//       <button onClick={generateResponse}>Generate Response</button>
//       <div className="response">
//         <h2>Response:</h2>
//         <p>{output}</p>
//       </div>
//     </div>
//   );
// }

// export default App;



import React, { useState } from 'react';
import axios from 'axios';
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState('');
  const [output, setOutput] = useState('');

  function handleChange(event) {
    setPrompt(event.target.value);
  }

  // console.log(prompt);
  async function generateResponse() {
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/generate",
        { prompt: prompt }
      );

      console.log(res.data.response);
      setOutput(res.data.response);
    } catch (error) {
      console.error(error);
      setOutput("Error generating response.");
    }
  }

  return (
    <div className="App">
      <h1>Mini Gemini Project</h1>
      <textarea
        onChange={handleChange}
        placeholder="Enter your text here..."
        rows={10}
        cols={50}
      ></textarea>
      <br />
      <button onClick={generateResponse}>Generate Response</button>
      <div className="response">
        <h2>Response:</h2>
        <p>{output}</p>
      </div>
    </div>
  );
}

export default App;