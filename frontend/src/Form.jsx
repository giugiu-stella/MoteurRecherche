import { useState } from 'react'
import './book.css'

const urlBaseRequete = 'http://127.0.0.1:8000/server/books/?'

function MyForm () {
    const [keyword, setKeyword] = useState('');
    const [title, setTitle] = useState('');
    const [selectedTitleType, setSelectedTitleType] = useState('classique');
    const [selectedKeywordType, setSelectedKeywordType] = useState('classique');
    const [selectedLanguage, setSelectedLanguage] = useState('en');
    const [selectedSort, setSelectedSort] = useState('download_count');
    const [selectedOrder, setSelectedOrder] = useState('ascending');
    const [author, setAuthor] = useState('');
    const [selectedAuthorType, setSelectedAuthorType] = useState('classique');

    const [bookData, setBookData] = useState(null);

    
    const onSubmit = () => {
        var url = urlBaseRequete + "sort=" + selectedSort + "&ord=" + selectedOrder

        if (selectedLanguage != "all") {
            url += "&language=" + selectedLanguage
        }

        if (author) {
            url += "&author_name=" + author + "&author_name_type=" + selectedAuthorType
        }

        if (title) {
            url += "&title=" + title + "&title_name_type=" + selectedTitleType
        }

        if (keyword) {
            url += "&keyword=" + keyword + "&keyword_type=" + selectedKeywordType
        }

        fetch(url, {
            mode: 'cors',
        })
        .then((response) => response.json())
        .then((result) => console.log(result) & setBookData(result))
        .catch((error) => console.error('Error fetching the books:', error));
      
    };
  
    return (
      <div>
        <h1>Search Engine</h1>
        <label>
            Keyword 
            <input type="text" value={keyword} onChange={(e) => setKeyword(e.target.value)} />
        </label>
        <label style={{ marginLeft: '10px' }}>
            Select a type:
            <select value={selectedKeywordType} onChange={(e) => setSelectedKeywordType(e.target.value)}>
            <option value="classique">classique</option>
            <option value="regex">regex</option>
            </select>
        </label>
        <br />
        <label>
            Title
        <input value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <label style={{ marginLeft: '10px' }}>
            Select a type:
            <select value={selectedTitleType} onChange={(e) => setSelectedTitleType(e.target.value)}>
            <option value="classique">classique</option>
            <option value="regex">regex</option>
            </select>
        </label>
        <br />
        <label>
            Author
        <input value={author} onChange={(e) => setAuthor(e.target.value)} />
        </label>
        <label style={{ marginLeft: '10px' }}>
            Select a type:
            <select value={selectedAuthorType} onChange={(e) => setSelectedAuthorType(e.target.value)}>
            <option value="classique">classique</option>
            <option value="regex">regex</option>
            </select>
        </label>
        <br />
        <label style={{ marginLeft: '10px' }}>
            Select a language:
            <select value={selectedLanguage} onChange={(e) => setSelectedLanguage(e.target.value)}>
                <option value="all">all</option>
                <option value="fr">french</option>
                <option value="en">english</option>
            </select>
        </label>
        <label style={{ marginLeft: '10px' }}>
            Select how to sort:
            <select value={selectedSort} onChange={(e) => setSelectedSort(e.target.value)}>
                <option value="download count">download count</option>
                <option value="closeness">closeness</option>
                <option value="betweenness">betweenness</option>
            </select>
        </label>
        <label style={{ marginLeft: '10px' }}>
            Select the order:
            <select value={selectedOrder} onChange={(e) => setSelectedOrder(e.target.value)}>
                <option value="ascending">ascending</option>
                <option value="descending">descending</option>
            </select>
        </label>
        <br />
        <button onClick={onSubmit}>Submit</button>
        <div className='container'>
      <div className="books-column">
      <h2>List of Books</h2>
        {bookData['result'].map((book, index) => (
            <div key={index} className="book">
            <h3>{book.title}</h3>
            <p>Authors: 
              {book.authors.map((author) => (
                <p>{author.name}</p>
              ))}</p>
            <img src={book.cover_image} alt={`Cover of ${book.title}`} style={{ maxWidth: '100px' }} />
            </div>
        ))}
      </div>
      <div className="suggestions-column">
        <h2>Suggestions</h2>
        {bookData['suggestion'].map((book, index) => (
            <div key={index} className="book">
            <h3>{book.title}</h3>
            <p>Authors: 
              {book.authors.map((author) => (
                <p>{author.name}</p>
              ))}</p>
            <img src={book.cover_image} alt={`Cover of ${book.title}`} style={{ maxWidth: '100px' }} />
            </div>
        ))}
        </div>
    </div>
      </div> 
      
    );
  };

  export default MyForm