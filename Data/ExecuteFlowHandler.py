import os
from . import ActionFlow

def loadFlow(flowName):
    path = "./Saved/" + flowName;
    if (os.path.exists(path)):
        f = open(path, "r")
        stream = f.read()
        f.close();
        return ActionFlow.ActionFlow.Deserialize(stream);
    else:
        return None;

def ExecuteFlow(initialFlow):
    stack = []
    stack.append(initialFlow);
    while (len(stack) > 0):
        flow = stack[-1];
        newFlowName = flow.ExecuteFlow();
        if (newFlowName == None):
            print("Flow ended naturally")
            stack.pop();
            continue;
        flow = loadFlow(newFlowName);

        if (flow == None):
            print("Faied to generate new flow");
            return;
        flow.Name = newFlowName;
        stack.append(flow);
