import React, { useState, useEffect } from 'react';
import { useSearch } from './Search';

const urlBaseRequete = 'http://127.0.0.1:8000/books/'

const FetchBook = () => {
  const { query, parameter } = useSearch();
  const [bookData, setBookData] = useState(null);

  useEffect(() => {
    var url = urlBaseRequete + query + parameter
    fetch(url)
    .then((response) => response.json())
    .then((result) => setBookData(result))
    .catch((error) => console.error('Error fetching the books:', error));
  }, [query, parameter ]); 

  return (
    <div>
        <p>Loading</p>
    </div>
  );
};

export default FetchBook;
