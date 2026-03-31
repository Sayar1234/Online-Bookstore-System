import '@testing-library/jest-dom';

// Fix for TextEncoder not defined in jest
import { TextEncoder, TextDecoder } from 'util';

Object.assign(global, {
  TextEncoder,
  TextDecoder,
});
