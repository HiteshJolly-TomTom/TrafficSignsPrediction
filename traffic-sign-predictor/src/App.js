import React, { useState } from 'react';
import Dropzone from 'react-dropzone';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const onDrop = (acceptedFiles) => {
    setFile(acceptedFiles[0]);
  };

  const uploadFile = () => {
    const formData = new FormData();
    formData.append('file', file);

    axios.post('http://localhost:5000/upload', formData)
      .then(response => setResult(response.data.result))
      .catch(error => console.error('Error:', error));
  };

  return (
    <div className="App">
      <h1>Traffic Sign Predictor</h1>
      <Dropzone onDrop={onDrop} accept=".shp,.zip">
        {({ getRootProps, getInputProps }) => (
          <div {...getRootProps()} style={{ border: '2px dashed #cccccc', padding: '20px', cursor: 'pointer' }}>
            <input {...getInputProps()} />
            <p>Drag 'n' drop a shapefile here, or click to select one</p>
          </div>
        )}
      </Dropzone>
      {file && <p>Selected file: {file.name}</p>}
      <button onClick={uploadFile}>Upload</button>
      {result !== null && <p>Predicted number of traffic signs: {result}</p>}
    </div>
  );
}

export default App;
