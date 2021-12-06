import { useEffect, useState } from 'react';
import axios from 'axios';

const useCollectData = (url) => {
    console.log("opening the connection, retreiving data")
    const [fetch, setFetching] = useState({ isFetching: false });
    const [dataState, setDataState] = useState({ data: [] });
    const [apiurl] = useState(url); // in order to get different api urls and set it to the state.

    useEffect(() => {
        const fetchDataFromApi = async () => {

            try{
                setFetching({isFectching: true}) // change the state first

                const response = await axios.get(apiurl) // get data from api using axios

                setDataState({...dataState, data: response.data}); // add new data coming from API what we have already

            } catch (e) {
                setFetching({ ...fetch, isFetching: true})
            }
        };
        fetchDataFromApi(); // call the function to  bring data as this ConnectApi file called

    }, []);// eslint-disable-line react-hooks/exhaustive-deps

    return [dataState] // return what is collected

};

export default useCollectData