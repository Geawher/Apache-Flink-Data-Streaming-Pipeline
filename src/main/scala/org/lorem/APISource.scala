package org.lorem

import org.apache.flink.streaming.api.functions.source.SourceFunction
import requests._

class APISource extends SourceFunction[String] {
  private var running: Boolean = true
  override def run(ctx: SourceFunction.SourceContext[String]): Unit = {
    while (running) {
      val response: Response = requests.get(
        "https://realstonks.p.rapidapi.com/TSLA",
        headers = Map(
          "X-RapidAPI-Key" -> "55add96f10msh5134a9505f7a1b6p189066jsna4ae3feb346f",
          "X-RapidAPI-Host" -> "realstonks.p.rapidapi.com"
        )
      )
      ctx.collect(response.text())
      Thread.sleep(5000)
    }
  }

  override def cancel(): Unit = {
    running = false
  }
}
