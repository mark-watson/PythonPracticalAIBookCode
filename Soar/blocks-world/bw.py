import Python_sml_ClientInterface as sml

def callback_debug(mid, user_data, agent, message):
    print(message)

if __name__ == "__main__":
    soar_kernel = sml.Kernel.CreateKernelInCurrentThread()
    soar_agent = soar_kernel.CreateAgent("agent")
    soar_agent.RegisterForPrintEvent(sml.smlEVENT_PRINT, callback_debug, None) # no user data
    soar_agent.ExecuteCommandLine("source bw.soar")
    run_result=soar_agent.RunSelf(50)
    soar_kernel.DestroyAgent(soar_agent)
    soar_kernel.Shutdown()
