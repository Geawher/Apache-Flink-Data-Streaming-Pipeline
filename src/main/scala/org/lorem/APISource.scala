package org.lorem

import com.typesafe.config.{Config, ConfigFactory}
import org.apache.flink.streaming.api.functions.source.SourceFunction
import requests._
import play.api.libs.json._

class APISource extends SourceFunction[Stock] {
  private var running: Boolean = true
  // Load application.conf in resources
  private val config: Config = ConfigFactory.load()
  // Utility class to
  override def run(ctx: SourceFunction.SourceContext[Stock]): Unit = {
    while (running) {
      // GET request
      val response: Response = requests.get(
        "https://realstonks.p.rapidapi.com/TSLA",
        headers = Map(
          "X-RapidAPI-Key" -> config.getString("API_KEY"),
          "X-RapidAPI-Host" -> "realstonks.p.rapidapi.com"
        )
      )
      val json: JsObject = Json.parse(response.text()).as[JsObject]
      val stock = new Stock(
        price = (json \ "price").as[Double],
        changePoint = (json \ "change_point").as[Double],
        changePercentage = (json \ "change_percentage").as[Double],
        totalVal = (json \ "total_vol").as[String]
      )
      // Emit response
      ctx.collect(stock)
      // Wait 1000ms for next request
      Thread.sleep(1000)
    }
  }

  override def cancel(): Unit = {
    running = false
  }
}
