import React, { createContext, useContext, useState } from 'react';

const SearchContext = createContext();



export const useSearch = () => {
  return useContext(SearchContext);
};
