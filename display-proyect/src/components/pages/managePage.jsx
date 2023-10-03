import React from 'react';
import TableItems from '../tableItems'
import EditItem from '../editItem';

import Container from 'react-bootstrap/Container';
import 'bootstrap/dist/css/bootstrap.css';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function Manage() {
  return (
    <Container>
      <Row>
        <Col md={6}>
          <TableItems />
        </Col>
        <Col md={6}>
          <EditItem />
        </Col>
      </Row>
    </Container>
  );
}

export default Manage;