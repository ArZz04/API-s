import React from 'react';
import Pagination from 'react-bootstrap/Pagination';

function CustomPagination({ activePage, totalPages, onPageChange }) {
  const items = [];
  
  for (let number = 1; number <= totalPages; number++) {
    items.push(
      <Pagination.Item
        key={number}
        active={number === activePage}
        onClick={() => onPageChange(number)}
      >
        {number}
      </Pagination.Item>
    );
  }

  return (
    <Pagination>
      {items}
    </Pagination>
  );
}

export default CustomPagination;