import { useState } from "react";
import "./essai.css";

const urlBaseRequete = "http://127.0.0.1:8000/server/books/?";

function MyForm() {
  const [keyword, setKeyword] = useState("");
  const [title, setTitle] = useState("");
  const [selectedTitleType, setSelectedTitleType] = useState("classique");
  const [selectedKeywordType, setSelectedKeywordType] = useState("classique");
  const [selectedLanguage, setSelectedLanguage] = useState("en");
  const [selectedSort, setSelectedSort] = useState("download_count");
  const [selectedOrder, setSelectedOrder] = useState("ascending");
  const [author, setAuthor] = useState("");
  const [selectedAuthorType, setSelectedAuthorType] = useState("classique");

  const [bookData, setBookData] = useState({ result: [], suggestion: [] });

  const onSubmit = () => {
    var url = urlBaseRequete + "sort=" + selectedSort + "&ord=" + selectedOrder;

    if (selectedLanguage != "all") {
      url += "&language=" + selectedLanguage;
    }

    if (author) {
      url +=
        "&author_name=" + author + "&author_name_type=" + selectedAuthorType;
    }

    if (title) {
      url += "&title=" + title + "&title_name_type=" + selectedTitleType;
    }

    if (keyword) {
      url += "&keyword=" + keyword + "&keyword_type=" + selectedKeywordType;
    }

    fetch(url, {
      mode: "cors",
    })
      .then((response) => response.json())
      .then((result) => setBookData(result))
      .catch((error) => console.error("Error fetching the books:", error));
  };

  const styles = {
    navbar: {
      height: "50px",
      width: "100%",
      backgroundColor: "grey",
      display: "flex",
      justifyContent: "space-between",
      padding: "20px",
    },
    logo: {
      color: "white",
      fontSize: "20px",
      fontWeight: "bold",
    },
    navItems: {
      display: "flex",
      alignItems: "center",
    },
    navLink: {
      color: "white",
      marginLeft: "20px",
      cursor: "pointer",
    },
    container: {
      display: "flex",
      marginTop: "30px",
      textAlign: "center",
    },
    containerForm: {
      display: "flex",
      alignItems: "center",
      marginTop: "30px",
    },
    formContainer: {
      width: "400px",
      padding: "20px",
      border: "1px solid #ccc",
      borderRadius: "8px",
      backgroundColor: "#f9f9f9",
    },
    label: {
      marginBottom: "10px",
      display: "block",
      with: "100px",
    },
    input: {
      width: "100%",
      height: "30px",
      margin: "8px 0",
      display: "inline-block",
      border: "1px solid #767474",
      borderRadius: "7px",
      textAlign: "center",
    },
    select: {
      width: "100%",
      height: "30px",
      margin: "8px 0",
      display: "inline-block",
      border: "1px solid #767474",
      borderRadius: "7px",
      textAlign: "center",
      marginLeft: "10px",
    },
    button: {
      marginTop: "20px",
      backgroundColor: "#4285f4",
      color: "white",
      border: "none",
      padding: "10px 20px",
      textAlign: "center",
      textDecoration: "none",
      fontSize: "16px",
      borderRadius: "5px",
      cursor: "pointer",
    },
    bookContainer: {
      display: "flex",
      justifyContent: "space-between",
      marginBottom: "20px",
    },
    bookDetails: {
      marginLeft: "10px",
      textAlign: "left",
    },
    bookImage: {
      maxWidth: "100px",
    },
    booksColumn: {
      marginLeft: "100px",
    },
    SuggestionColumn: {
      marginLeft: "100px",
    },
  };

  return (
    <div>
      <div style={styles.navbar}>
        <div style={styles.logo}>Search Engine</div>
      </div>
      <div style={styles.container}>
        <div style={styles.formContainer}>
          <h2>Search for a book</h2>
          <div style={styles.containerForm}>
            <label style={styles.label}>
              Keyword
              <input
                type="text"
                value={keyword}
                onChange={(e) => setKeyword(e.target.value)}
                style={styles.input}
                placeholder="Enter a keyword"
              />
            </label>

            <label style={styles.label}>
              Select a type:
              <select
                value={selectedKeywordType}
                onChange={(e) => setSelectedKeywordType(e.target.value)}
                style={styles.select}
              >
                <option value="classique">classique</option>
                <option value="regex">regex</option>
              </select>
            </label>
          </div>
          <div style={styles.containerForm}>
            <label style={styles.label}>
              Title
              <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                style={styles.input}
                placeholder="Enter a Title"
              />
            </label>
            <label style={styles.label}>
              Select a type:
              <select
                value={selectedTitleType}
                onChange={(e) => setSelectedTitleType(e.target.value)}
                style={styles.select}
              >
                <option value="classique">classique</option>
                <option value="regex">regex</option>
              </select>
            </label>
          </div>
          <div style={styles.containerForm}>
            <label style={styles.label}>
              Author
              <input
                type="text"
                value={author}
                onChange={(e) => setAuthor(e.target.value)}
                style={styles.input}
                placeholder="Enter an author"
              />
            </label>
            <label style={styles.label}>
              Select a type:
              <select
                value={selectedAuthorType}
                onChange={(e) => setSelectedAuthorType(e.target.value)}
                style={styles.select}
              >
                <option value="classique">classique</option>
                <option value="regex">regex</option>
              </select>
            </label>
          </div>
          <div style={styles.containerForm}>
            <label style={styles.label}>
              Select a language:
              <select
                value={selectedLanguage}
                onChange={(e) => setSelectedLanguage(e.target.value)}
                style={styles.select}
              >
                <option value="all">all</option>
                <option value="fr">french</option>
                <option value="en">english</option>
              </select>
            </label>

            <label style={{ ...styles.label, marginLeft: "10px" }}>
              Select how to sort:
              <select
                value={selectedSort}
                onChange={(e) => setSelectedSort(e.target.value)}
                style={{ ...styles.select, marginTop: "25px" }}
              >
                <option value="download count">download count</option>
                <option value="closeness">closeness</option>
                <option value="betweenness">betweenness</option>
              </select>
            </label>
            <label style={{ ...styles.label, marginLeft: "10px" }}>
              Select the order:
              <select
                value={selectedOrder}
                onChange={(e) => setSelectedOrder(e.target.value)}
                style={{ ...styles.select, marginTop: "25px" }}
              >
                <option value="ascending">ascending</option>
                <option value="descending">descending</option>
              </select>
            </label>
          </div>
          <button onClick={onSubmit} style={styles.button}>
            Search
          </button>
        </div>
        <div className="container">
          <div style={styles.booksColumn}>
            <h2>List of Books</h2>
            {bookData["result"].map((book, index) => (
              <div key={index} style={styles.bookContainer}>
                <div style={styles.bookDetails}>
                  <h3>{book.title}</h3>
                  <p>
                    Authors:
                    {book.authors.map((author, authorIndex) => (
                      <p key={authorIndex}>{author.name}</p>
                    ))}
                  </p>
                </div>
                <img
                  src={book.cover_image}
                  alt={`Cover of ${book.title}`}
                  style={styles.bookImage}
                />
              </div>
            ))}
          </div>
          <div style={styles.SuggestionColumn}>
            <h2>Suggestions</h2>
            {bookData["suggestion"].map((book, index) => (
              <div key={index} style={styles.bookContainer}>
                <div style={styles.bookDetails}>
                  <h3>{book.title}</h3>
                  <p>
                    Authors:
                    {book.authors.map((author, authorIndex) => (
                      <p key={authorIndex}>{author.name}</p>
                    ))}
                  </p>
                </div>
                <img
                  src={book.cover_image}
                  alt={`Cover of ${book.title}`}
                  style={styles.bookImage}
                />
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default MyForm;
