package org.lorem

/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import org.apache.commons.math3.stat.descriptive.moment.Mean
import org.apache.flink.api.common.functions.AggregateFunction
import org.apache.flink.api.common.serialization.SimpleStringEncoder
import org.apache.flink.api.scala._
import org.apache.flink.core.fs.Path
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.dataformat.csv.CsvSchema
import org.apache.flink.streaming.api.functions.sink.filesystem.StreamingFileSink
import org.apache.flink.streaming.api.functions.sink.filesystem.rollingpolicies.DefaultRollingPolicy
import org.apache.flink.streaming.api.scala.{DataStream, StreamExecutionEnvironment}
import org.apache.flink.streaming.api.windowing.assigners.{SlidingEventTimeWindows, SlidingProcessingTimeWindows}
import org.apache.flink.streaming.api.windowing.time.Time

import java.util.concurrent.TimeUnit

class AverageAggregate extends AggregateFunction[Stock, (Double, Int), Double] {
  override def createAccumulator(): (Double, Int) = (0.0, 0)
  override def add(value: Stock, accumulator: (Double, Int)): (Double, Int) = (accumulator._1 + value.price, accumulator._2 + 1)
  override def getResult(accumulator: (Double, Int)): Double = accumulator._1 / accumulator._2
  override def merge(a: (Double, Int), b: (Double, Int)): (Double, Int) = (a._1 + b._1, a._2 + b._2)
}
object Job {
  def main(args: Array[String]): Unit = {
    // set up the execution environment
    val env = StreamExecutionEnvironment.getExecutionEnvironment

    val sink: StreamingFileSink[Double] = StreamingFileSink
      .forRowFormat(new Path("C:\\Users\\nizar\\OneDrive\\Bureau"), new SimpleStringEncoder[Double]("UTF-8"))
      .withRollingPolicy(
        DefaultRollingPolicy.builder()
          .withRolloverInterval(TimeUnit.MINUTES.toMillis(15))
          .withInactivityInterval(TimeUnit.MINUTES.toMillis(5))
          .withMaxPartSize(1024 * 1024 * 1024)
          .build())
      .build()

    // Read data stream =  ..., {"price": 185.45, "change_point": -0.07, "change_percentage": -0.04, "total_vol": "133.88M"}, ...
    val dataStream: DataStream[Stock] = env.addSource(new APISource)
    dataStream
      .keyBy( _.id )
      .windowAll(SlidingProcessingTimeWindows.of(Time.seconds(10), Time.seconds(5))) // Flink sliding window
      .aggregate(new AverageAggregate)
      .addSink(sink)


    // execute program
    env.execute("Flink Scala API Skeleton")
  }
}
