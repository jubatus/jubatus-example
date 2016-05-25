package us.jubat.example.slot;

import org.apache.commons.math3.random.RandomDataGenerator;

import java.util.Random;

public class SlotMachine {
    private float hitRate;
    private float averageValue;
    private float standardDeviation;

    private static int SHEED = 0;
    private static Random random = new Random(SHEED);

    public SlotMachine(float hitRate, float averageValue, float standardDeviation) {
        this.hitRate = hitRate;
        this.averageValue = averageValue;
        this.standardDeviation = standardDeviation;
    }

    public boolean hit(){
        return (SlotMachine.random.nextFloat() < hitRate);
    }

    public float generateReward(){
        if(hit()){
            //ガウス分布に従う乱数を生成する。
            RandomDataGenerator generator = new RandomDataGenerator();
            double reward = generator.nextGaussian(averageValue , standardDeviation);
            return (float)reward;
        }else {
            return 0;
        }
    }
}
