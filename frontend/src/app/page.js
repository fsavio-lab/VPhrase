'use client'
import styles from "./page.module.css";
import { useEffect, useState } from "react";
import axios from 'axios';
import { LineChart } from '@mui/x-charts/LineChart';
import { MOVIES_URL } from "./constants";
import { BarChart } from "@mui/x-charts";
import useWindowDimensions from "./windowDimensions";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import {
  blueberryTwilightPalette,
  mangoFusionPalette,
  cheerfulFiestaPalette,
} from '@mui/x-charts/colorPalettes';
const colourPallete = {
  "Blueberry Twilight": blueberryTwilightPalette,
  "Mango Fusion": mangoFusionPalette,
  "Cheerful Fiesta": cheerfulFiestaPalette
}

export default function Home() {
  const [isDataFetched, setIsDataFetched] = useState(false)
  const [lineChartData, setLineChartData] = useState([]);
  const [barChartData, setBarChartData] = useState([]);
  const [chartData, setChartData] = useState([]);

  const YEAR = 2017

  let fetchData = (url,state_handler) => {
    axios.get(url, {
      headers: {
        "Content-Type": "application/json"
      }
    }).then(response => response.data).then(data => {
      let stored_data = data
      state_handler(stored_data)
    })
  }

  useEffect(() => {
    fetchData(`${MOVIES_URL}?format=json&order_by=votes desc&size=5`,setLineChartData)
    // console.log(`${MOVIES_URL}?format=json`)
    fetchData(`${MOVIES_URL}?format=json&year=${YEAR}&order_by=grossing_value desc&size=5`,setBarChartData)
    // console.log(`${MOVIES_URL}?format=json&year=${YEAR.toString()}&order_by=grossing_value desc&page=5`)
    fetchData(`${MOVIES_URL}?format=json&year=${YEAR}&order_by=rating desc&size=10`,setChartData)
    // console.log(`${MOVIES_URL}?format=json&year=${YEAR.toString()}&order_by=grossing_value desc&page=5`)
    setIsDataFetched(true)
  }, [])

  const [colorScheme, setColorScheme] = useState(colourPallete["Cheerful Fiesta"])
  const chartTheme = createTheme({ palette: { mode: "dark" } })

  return (
    <ThemeProvider theme={chartTheme}>
      <div>
        <div className={styles.header}>
          <h1>Data Visualization Assignment</h1>
        </div>
        <main className={styles.main}>
          <div className={styles.center}>
            <div className={styles.card}>
              <h3 className={styles.title}>Top 5 movies based on gross earnings for year {YEAR}</h3>
              <BarChart
                series={
                  [{
                    label: "Gross Earnings",
                    data: barChartData.map((x) => x.grossing_value),
                    // area: true
                  }]
                }
                xAxis={[{ scaleType: "band", data: barChartData.map(x => x.name) }]}
                height={500}
                width={useWindowDimensions().width}
                margin={{ top: 30, bottom: 30, right: 128, left: 128 }}
                colors={colorScheme}
              />
            </div>
            <div className={styles.card}>
              <h3 className={styles.title}>Top 5 movies of all time according to votes</h3>
              <LineChart
                // dataset={data.map((x) => x.votes)}
                xAxis={[{ scaleType: "point", data: lineChartData.map(x => x.name) }]}
                series={[{
                  label: "Votes",
                  data: lineChartData.map((x) => x.votes),
                  // area: true
                }]}
                height={500}
                width={useWindowDimensions().width}
                margin={{ top: 30, bottom: 30, right: 128, left: 128 }}
                colors={colorScheme}
                yAxis={[{ 
                  min: Math.min(...lineChartData.map(e => e.votes)) - (Math.min(...lineChartData.map(e => e.votes)) / lineChartData.length),
                  max: Math.max(...lineChartData.map(e => e.votes)) + (Math.min(...lineChartData.map(e => e.votes)) / lineChartData.length) 
                }]}
              />
            </div>

            <div className={styles.card}>
              <h3 className={styles.title}>Top 5 movies based on ratings for year {YEAR}</h3>
              <BarChart
                series={
                  [{
                    label: "Ratings",
                    data: chartData.map((x) => x.rating),
                    area: true
                  }]
                }
                xAxis={[{ scaleType: "band", data: chartData.map(x => x.name) }]}
                yAxis={[{ min: Math.min(...chartData.map(e => e.rating)) - 0.1, max: Math.max(...chartData.map(e => e.rating)) }]}
                height={500}
                width={useWindowDimensions().width}
                colors={colorScheme}
              />
            </div>
          </div>
        </main>
        <div className={styles.footer}>
          <h1>Developed by Savio Fernando</h1>
        </div>
      </div>
    </ThemeProvider>

  );
}
