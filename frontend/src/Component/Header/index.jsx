import { faSearch } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './index.css';

function Search() {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = () => {
    console.log("검색어:", searchTerm);
  };

  const handleChange = (event) => {
    setSearchTerm(event.target.value);
  };

  return (
    <div className='header-container'>
      <div className='header-title'>
        <h2> (logo) Dog<span>Go</span></h2>
      </div>
      <div className='header-search'>
        <div className='header-search_input'>
          <input
            type="text"
            placeholder="검색어를 입력하세요"
            value={searchTerm}
            onChange={handleChange}
          />
          <div className='header-search_icon'
           onClick={handleSearch}>
            <FontAwesomeIcon icon={faSearch} />
          </div>
        </div>
      </div>
      <div className='header-login'>
        <ul>
          <span>웰컴</span>
          <Link><li>로그인</li></Link>
          <Link><li>고객센터</li></Link>
        </ul>
      </div>
    </div>
  );
}

export default Search;