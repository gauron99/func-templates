'use strict';
import { start, InvokerOptions } from 'faas-js-runtime';
import request from 'supertest';

import * as func from '../build';
import test, { Test } from 'tape';

const data = { message: 'Hello Typescript World!' };

const errHandler = (t: Test) => (err: Error) => {
  t.error(err);
  t.end();
};

test('Integration: handles a valid request', (t) => {
  start(func.handle, {} as InvokerOptions).then((server) => {
    t.plan(3); //t.error,t.ok,t.equal
    request(server)
      .post('/')
      .send({}) // send empty request
      .expect(200)
      .expect('Content-Type', /json/)
      .end((err, result) => {
        t.error(err, 'expected no error');
        t.ok(result);
        // NOTE: Server returns Hello World, regardless of the data sent.
        // TODO: You can change the server (index.ts) to return some data and
        // validate it here by changing this string to that data.
        t.deepEqual(JSON.stringify(result.body), JSON.stringify(data));
        server.close();
        t.end();
      });
  }, errHandler(t));
});
