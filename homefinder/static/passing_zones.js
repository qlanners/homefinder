var passingZones = function(zones_complete) {
    var svg2 = d3.select("#second_svg")
    var div = d3.select("#second_svg_tooltip")
	svg2.selectAll("rect").data(zones_complete).enter().append("rect").attr("height","250")
	.attr("width","200")
	.attr("x",function(d,i){return 197+((i%3)*200)}).attr("y",function(d,i) { if(i<3){return "286"} return"36" }).attr("fill",function(d,i) { if((d[0]/(d[0]+d[1]))<0.5){return "red"} return"green" }).attr("opacity",function(d,i){return (d[0]/(d[0]+d[1]))*0.5 }).attr("stroke","black")
  .on("mouseover", function(d,i){ 
    d3.select(this).attr("fill","blue")
    var xPosition = 40+parseFloat(d3.select(this).attr("x"))+(parseFloat(d3.select(this).attr("width"))/2)
    var yPosition = parseFloat(d3.select(this).attr("y")) + 500
    div.transition()    
                  .duration(200)    
                  .style("opacity", .9);    
              div.html(d[0] + " completions (" + (d[0]/(d[0]+d[1])).toFixed(2)*100 + " Cmp%)")
                  .style("left", xPosition + "px")   
                  .style("top", yPosition + "px");  
              })      
        .on("mouseout", function(d) {  
              d3.select(this).attr("fill",function(d,i) { if((d[0]/(d[0]+d[1]))<0.5){return "red"} return"green" })
              div.transition()    
                  .duration(500)    
                  .style("opacity", 0); 
        });

	svg2.append("text").text("Deep").attr("x","110").attr("y","170").attr("font-size","30")
	svg2.append("text").text("Short").attr("x","110").attr("y","420").attr("font-size","30")
	svg2.append("text").text("Left").attr("x","250").attr("y","30").attr("font-size","30")
	svg2.append("text").text("Middle").attr("x","450").attr("y","30").attr("font-size","30")
	svg2.append("text").text("Right").attr("x","650").attr("y","30").attr("font-size","30")
}  

function update(){
        var seasons = [];
        d3.selectAll(".myCheckbox").each(function(d){
          cb = d3.select(this);
          if(cb.property("checked")){
            seasons.push(cb.property("value"));
          }
        });
      	var arrayLength = seasons.length
        var zones_complete_newData = [0,0,0,0,0,0]
        var zones_incomplete_newData = [0,0,0,0,0,0]

        if(seasons.length > 0){
          for(var i = 0; i < arrayLength; i++) { zones_complete_newData = zones_complete_newData.map(function(num,idx){ return num + passing_zones_complete[seasons[i]][idx];})}   
          for(var i = 0; i < arrayLength; i++) { zones_incomplete_newData = zones_incomplete_newData.map(function(num,idx){ return num + passing_zones_incomplete[seasons[i]][idx];})}     
             
          	
        } else {
          zones_complete_newData = zones_complete_newData 
          zones_incomplete_newData = zones_incomplete_newData  
        }            
      
      	var attempts_new = []
		for (var i=0; i<zones_incomplete_newData.length; i++) {
			var year = [zones_complete_newData[i],zones_incomplete_newData[i]]
			attempts_new.push(year)
		}  
		
        passingZones(attempts_new)

    }