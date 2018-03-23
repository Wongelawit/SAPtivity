import React from 'react';
import GetLoc from './GetLoc';
import Graphs from './Graphs';
import TrackLoc from './TrackLoc';
import DailyToDo from './DailyToDo';
import WeeklyToDo from './WeeklyToDo';
import MonthlyToDo from './MonthlyToDo';

import { Platform, Text, View, StyleSheet, TouchableHighlight, Image, ScrollView } from 'react-native';

class App extends React.Component {

  constructor()
  {
    super()
    this.state = ({
      tab:0
    })
  }

  componentWillMount()
  {
  }

  onPress(clicked)
  {
    this.setState({
      tab:clicked
    })
  }

  render()
  {
    let content = <Text>Error</Text>
    let zero_style = styles.tabItem
    let one_style = styles.tabItem
    let two_style = styles.tabItem

    let zero_font = styles.tabText
    let one_font = styles.tabText
    let two_font = styles.tabText

    let title = null


    if (this.state.tab === 2)
    {
        two_style = styles.tabItem_active
        two_font = styles.tabText_active
        title = <MonthlyToDo/>
    }
    else if (this.state.tab === 1)
    {
        one_style = styles.tabItem_active
        one_font = styles.tabText_active
        title = <WeeklyToDo/>
    }
    else if (this.state.tab === 0)
    {
      zero_style = styles.tabItem_active
      zero_font = styles.tabText_active
      title = <DailyToDo/>
    }
    return(
      <ScrollView style={styles.navBar}>
        <View style={styles.headBar}>
          <Text style={styles.headText}>SAPtivity</Text>
        </View>
        <View style={styles.tabs_cont}>
          <TouchableHighlight onPress={() => this.onPress(0)} style={zero_style}>
            <Text style={zero_font}>Daily</Text>
          </TouchableHighlight>
          <TouchableHighlight onPress={() => this.onPress(1)} style={one_style}>
            <Text style={one_font}>Weekly</Text>
          </TouchableHighlight>
          <TouchableHighlight onPress={() => this.onPress(2)} style={two_style}>
            <Text style={two_font}>Monthly</Text>
          </TouchableHighlight>
        </View>
        {title}
        <TrackLoc/>
        <Graphs screen={this.state.tab}/>


      </ScrollView>

    )
  }
}

const styles = StyleSheet.create({
  headBar: {
    backgroundColor:'#003366',
    justifyContent:'center',
    height: 80
  },
  tabs_cont: {
    flex:1,
    flexDirection:'row',
    width:null,
    justifyContent:'center',
    alignItems: 'stretch',
  },
  tabItem: {
    justifyContent:'center',
    borderWidth:0.5,
    borderColor: 'black',
    width:110,
    height:50,
    backgroundColor:'#45679b',
  },
  tabItem_active: {
    justifyContent:'center',
    borderWidth:1,
    borderColor: 'black',
    borderBottomColor:'white',
    width:110,
    height:50,
    backgroundColor:'white',
  },
  navBar: {
    flex: 1,
    flexDirection:'column',
  },
  headText: {
    textAlign:'center',
    marginTop: 15,
    color:'white',
    fontSize:24,
    fontWeight:'bold',
    fontFamily:'AppleSDGothicNeo-Bold'
  },
  tabText: {
    fontWeight:'bold',
    textAlign:'center',
    color:'white'
  },
  tabText_active: {
    fontWeight:'bold',
    textAlign:'center',
    color:'#314460'
  }
})

export default App
