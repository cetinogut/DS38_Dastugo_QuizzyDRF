import React from 'react'
import { makeStyles } from "@material-ui/core/styles";
import { AppBar, Toolbar, Typography } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
      backgroundColor:'green'
    },
    appBar: {

    },
    toolbarTitle: {
      flexGrow: 1,
      backgroundColor: "yellow"
    }
  }));

//export default function Header() {
const Header = () => {
    const classes = useStyles();
    return (
        <div className={classes.root}>
            <AppBar position="static" color="default" elevation={0}  className={classes.appBar}>
                <Toolbar>
                <Typography
                    variant="h6"
                    color="inherit"
                    className={classes.toolbarTitle}
                >
                    Quizzes
                </Typography>
                </Toolbar>
            </AppBar>
        </div>
    )
}
export default Header;